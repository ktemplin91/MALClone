# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class MessageForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)



    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_id = 'post-form'
    helper.layout = Layout(
        Field('username', id = 'log_id', css_class='input-xlarge'),
        Field('password',  id='log_pass'),
        FormActions(
            Submit('submit', 'Log In', css_class="btn-primary"),
            Button('cancel', 'Cancel'),
        )
    )

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_id = 'new-user-form'
    helper.layout = Layout(
        Field('email', id='mail_id', css_class='input-xlarge', type='email'),
        Field('username', id='reg_id', css_class='input-xlarge'),
        Field('password', autocomplete='off'),
        FormActions(
            Submit('submit', 'Register', css_class="btn-primary"),
            Button('cancel', 'Cancel'),
        )
    )
