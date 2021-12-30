from django_registration.forms import RegistrationForm
from users.models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        # fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False
            self.helper.layout = Layout(
                #This is a syntax error
                Field('username', data_label_text="whatever")
            )
            self.helper.add_input(Submit('submit', 'Submit'))