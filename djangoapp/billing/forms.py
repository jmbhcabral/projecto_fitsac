from django import forms
from billing.models import Pack, Payment, Subscription, Invoice
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class PackForm(forms.ModelForm):
    ''' Pack form '''
    class Meta:
        ''' Meta '''
        model = Pack
        fields = ['name', 'description', 'price', 'order', 'is_active']

    name = forms.CharField(
        label='Nome',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )
    description = forms.CharField(
        label='Descrição',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }
        )
    )
    price = forms.DecimalField(
        label='Preço',
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }
        )
    )
    order = forms.IntegerField(
        label='Ordem',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Order'
            }
        )
    )
    is_active = forms.BooleanField(
        label='Ativo',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        ''' Clean '''
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')

        errors = {}

        if not name:
            errors['name'] = 'O nome é obrigatório'

        # Get the instance id if it exists
        instance_id = self.instance.id

        if name:
            # Ckeck if the name already exists, excluding self instance
            if Pack.objects.filter(name=name).exclude(id=instance_id).exists():
                errors['name'] = 'Já existe um pack com este nome'

            name_len = len(name)
            excess = self.fields['name'].max_length - name_len
            if name_len < 3:
                errors['name'] = (
                    f'O nome deve ter no mínimo 3 caracteres.')

            if name_len > 20:
                errors['name'] = (
                    f'O nome deve ter no máximo 20 caracteres, tem {excess} caracteres a mais')

        if not price:
            errors['price'] = 'O preço é obrigatório'

        if description:
            description_len = len(description)
            excess = description_len - \
                self.fields['description'].max_length
            if description_len > 500:
                errors['description'] = (
                    f'A descrição deve ter no máximo 500 caracteres, tem {excess} caracteres a mais')

        if errors:
            raise forms.ValidationError(errors)
        return cleaned_data


class PackOrderForm(forms.Form):
    ''' Pack order form '''

    def __init__(self, *args, **kwargs):
        ''' Init '''

        # Receive the packs from the view dinamically
        packs = kwargs.pop('packs')
        super().__init__(*args, **kwargs)

        # Generate the fields dinamically
        for pack in packs:
            self.fields[str(pack.id)] = forms.IntegerField(
                label=pack.name,
                initial=pack.order,
                widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Order'
                    }
                )
            )

    def clean(self):
        ''' Clean '''
        cleaned_data = super().clean()
        errors = {}

        for field, value in cleaned_data.items():
            if value < 0:
                errors[field] = 'O valor deve ser maior ou igual a zero'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data


class PaymentForm(forms.ModelForm):
    ''' Payment form '''
    class Meta:
        model = Payment
        fields = ['invoice', 'date']

    invoice = forms.ModelChoiceField(
        label='Fatura',
        queryset=Invoice.objects.none(),  # Inicialmente vazio
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    date = forms.DateField(
        label='Data Pagamento',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        # Receber o utilizador da view
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            # Filtrar as faturas para o utilizador específico
            self.fields['invoice'].queryset = Invoice.objects.filter(user=user, status=False)

    def clean(self):
        ''' Clean '''
        user = self.data.get('user')
        cleaned_data = super().clean()
        invoice = cleaned_data.get('invoice')
        date = cleaned_data.get('date')

        errors = {}

        if not invoice:
            errors['invoice'] = 'A fatura é obrigatória'

        if user and Payment.objects.filter(user=user, invoice=invoice).exists():
            errors['invoice'] = 'Já existe um pagamento para este aluno neste mês/ano'

        if date:
            now = timezone.now().date()
            if date > now:
                errors['date'] = 'A data de pagamento deve ser menor ou igual à data atual'
        else:
            errors['date'] = 'A data de pagamento é obrigatória'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data


class PaymentUpdateForm(PaymentForm):
    ''' Payment update form '''

    class Meta:
        ''' Meta '''
        model = Payment
        fields = ['invoice', 'date']

    invoice = forms.ModelChoiceField(
        label='Fatura',
        queryset=Invoice.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control', }
        ),

    )

    date = forms.DateField(
        label='Data Pagamento',
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        )
    )

    def clean(self):
        ''' Clean '''
        cleaned_data = super().clean()
        invoice = cleaned_data.get('invoice')
        date = cleaned_data.get('date')

        errors = {}

        if not invoice:
            errors['invoice'] = 'A fatura é obrigatória'

        if date:
            now = timezone.now().date()
            if date > now:
                errors['date'] = 'A data de pagamento deve ser menor ou igual a data atual'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data


class SubscriptionForm(forms.ModelForm):
    ''' Subscription form '''
    class Meta:
        ''' Meta '''
        model = Subscription
        fields = ['user', 'pack', 'start_date', 'end_date']

    user = forms.ModelChoiceField(
        label='Aluno',
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        ''' Init '''
        super().__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = (
            lambda obj: f'{obj.first_name} {obj.last_name}'
        )

    pack = forms.ModelChoiceField(
        label='Pack',
        queryset=Pack.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    start_date = forms.DateField(
        label='Data de início',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )
    end_date = forms.DateField(
        label='Data de término',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        ),
        required=False
    )

    def clean(self):
        ''' Clean '''
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        pack = cleaned_data.get('pack')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        errors = {}

        instance_id = self.instance.id if self.instance else None

        if not user:
            errors['user'] = 'O aluno é obrigatório'

        if not pack:
            errors['pack'] = 'O pack é obrigatório'

        if pack:
            if not pack.is_active:
                errors['pack'] = 'O pack selecionado não está ativo'

        subs = Subscription.objects.filter(user=user, pack=pack)

        if instance_id:
            subs = subs.exclude(id=instance_id)

        if subs.filter(end_date__isnull=True).exists():
            errors['pack'] = (
                f'O aluno já possui uma subscrição ativa para o pack {pack}.'
            )

        if not start_date:
            errors['start_date'] = 'A data de início é obrigatória'

        if start_date and end_date:
            if start_date > end_date:
                errors['end_date'] = 'A data de término deve ser maior que a data de início'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
