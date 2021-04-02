# Padrão Strategy
O padrão Strategy é um padrão comportamental, ...

## Contexto
Vamos imaginar que você está para desenvolver uma funcionalidade que enviará diferentes e-mails para
o seus clientes via API. Outro detalhe, cada email tem o seu próprio template na plataforma que você 
usará para envia-los.

> Exemplo: envio de email utilizando a API do Mandrill. Neste addon da plataforma de Email 
> Marketing do Mailchimp, configuramos os templates com as informações que precisamos, e os enviamos
> utilizando uma API. 

O que temos então?
- Uma demanda para criar um service para enviar emails para nosso clientes
- Diferentes templates para diferentes situações

## O Problema
A priori, a solução é simples.
Criar um algortimo que eu preciso passar somente o nome do meu template como parâmetro para 
ele ser enviado!

```
... Na sua função que importa a lib do serviço de email ... 
# Função
def send_email_to_client(template_name):
    email_service = EmailService()

    email_service.send_email_template(template_name=template_name)

...
# Código
template_name = "EMAIL1"

send_email_to_client(template_name)
```

Até aqui... ok. Mas também temos outros templates pra se aplicar, e cada um com sua condição 
específica.

```
# Função
def send_email_to_client(template_name):
    email_service = EmailService()

    email_service.send_email_template(template_name=template_name)

...
# Código
if first_condition:
    template_name = "EMAILCONDICAO1"
elif second_condition:
    template_name = "EMAILCONDICAO2"
elif third_condition:
    template_name = "EMAILCONDICAO3"

send_email_to_client(template_name)
```
E existem muitas outras situações que você tera que enviar email. Imagine isso para 50+ diferentes
tipos de condições/templates.

- Será que cada vez que eu tiver um template novo eu vou precisar alterar esta função?
- E se um nome do template mudar, eu vou precisar alterar nessa função?
- Ela vai crescer infinitamente para cada template que eu tiver?
- Minha função precisa MESMO saber o nome do template, de forma explícita?

Neste momento o alerta já começa a apitar.

> Além disso, imagine quando você precisar enviar outros dados específicos de cada template e/ou do seu 
cliente. Mas não será neste padrão que entraremos nessa questão. ~~facade~~

## A possível solução
Bem, à principio temos que ter em mente que é sempre bom não alterar um código funcional para 
adicionar uma nova funcionalidade.

E, levando em considerações as questões levantadas, essa função pode trazer muita preocupação 
futuramente.

Então, devemos fazer com que possamos implementar templates novos, sendo que este deva ser mapeado
facilmente e que não fique completamente exposto a função, e que principalmente, não precisemos
alterar coisas que já funcionam. Além disso

#### Utilizando STRATEGY para resolver a situação
Podemos criar uma classe separada para cada template de email. 
Assim, podemos ajustar nossa função de envio de forma que ela consiga extrair as informações 
para enviar o email, deixando o nome do template protegido dentro da classe, e permitindo que 
novos templates sejam implementados sem que seja necessário modificar a função de envio de email.

A princípio nossos objetivos são esses: 
- Criar uma classe para cada template
- Modificar a classe de envio para compreender essa classe de template de email
```
# Função
def send_email_to_client(template):
    email_service = EmailService()

    template_name = template.template_name

    email_service.send_email_template(template_name=template_name)
...

class Email1:
    template_name = "EMAILCONDICAO1"

class Email2:
    template_name = "EMAILCONDICAO2"

class Email3:
    template_name = "EMAILCONDICAO3"
...

template = Email1()  # Pode ser EMAIL2 ou EMAIL3

send_email_to_client(template)

```
Com o strategy, nós criamos uma "família" de objetos semelhantes, que contem em dentro de si
as informaçães necessárias para nosso código.

Para aplicá-lo, nós extraimos da função de envio de email o parâmetro do nome do template, e 
o colocamos em uma classe, assim, invés de ter vários condicionais para verificar qual template
seria acionado, nós já recebemos o objeto dele, que é compreendido pela nossa função.

####### TODO Contar mais especificamente sobre as classes estratégias

## Como ajudou
Como podemos ver, o padrão Strategy pode nos ajudar muito a fazer com que o nosso código fique mais
seguro e flexível somente extraindo parametros em classes do mesmo tipo, e fazendo com que o nosso
"enviador de emails" compreenda objetos somente daquele tipo.

Além disso, ganhamos em manutenabilidade, aonde se precisamos atualizar o template de email para
alguma versão mais nova, alteramos somente a classe deste, sem precisar mexer na função principal.

# Conclusão
É claro que foi uma utlização bem simples para este caso, aonde somente o que diferencia cada template
é somente o nome dele.

####### TODO Colocar caso atual
 
####### TODO Revisar texto