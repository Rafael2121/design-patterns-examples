# TODO aplicar interface

# lib externa de envio de email
class EmailService:

    def send_email_template(self, template_name):
        print(f"Email {template_name} enviado com sucesso!")


## Objetos de email
class Email1:
    template_name = "EMAILCONDICAO1"

class Email2:
    template_name = "EMAILCONDICAO2"

class Email3:
    template_name = "EMAILCONDICAO3"


## Função de envio de email
def send_email_to_client(template):
    email_service = EmailService()

    template_name = template.template_name

    email_service.send_email_template(template_name=template_name)


template = Email1()  # Pode ser EMAIL2 ou EMAIL3

send_email_to_client(template)
