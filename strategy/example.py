# lib externa de envio de email
class EmailService:

    def send_email_template(self, template_name):
        print(f"Email {template_name} enviado com sucesso!")


class EmailTemplate:

    template_name = None

    def retrieve_email_data(self):
        return self.template_name

# --- Objetos de email


class Email1(EmailTemplate):
    template_name = "EMAILCONDICAO1"


class Email2(EmailTemplate):
    template_name = "EMAILCONDICAO2"


class Email3(EmailTemplate):
    template_name = "EMAILCONDICAO3"


## Função de envio de email
def send_email_to_client(template_obj: EmailTemplate):
    email_service = EmailService()

    template_name = template_obj.retrieve_email_data()

    email_service.send_email_template(template_name=template_name)


template_list = [Email1(), Email3()]

for template_obj in template_list:
    send_email_to_client(template_obj)
