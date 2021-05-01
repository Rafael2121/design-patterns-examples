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
- E se um nome do template mudar, eu vou precisar alterar essa função?
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
alterar coisas que já funcionam.

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
O strategy em si solicita que, você crie uma **classe contexto** que irá receber sua **classe
estratégia** como parâmetro, e independente de qual essa seja, o contexto deverá conseguir
executar a função "estretégia".

Como por exemplo, uma classe de envio de email(**contexto**) e as classes de templates de email
(**estratégia**) que contem uma função de "pegar dados do template". 

## Como ajudou
Como podemos ver, o padrão Strategy pode nos ajudar muito a fazer com que o nosso código fique mais
seguro e flexível somente extraindo parametros em classes do mesmo tipo, e fazendo com que o nosso
"enviador de emails" compreenda objetos somente daquele tipo.

Assim, fazemos com que nossos objetos tenham uma função que retorna os dados a serem utilizados
para o envio do email, permitindo tambem que cada uma retorne os dados específicos para cada caso.

Com isso, ganhamos em manutenabilidade, aonde se precisamos atualizar a classe template
de email para alguma versão mais nova, alteramos somente a classe deste, sem precisar mexer 
na função principal.

# Conclusão
É claro que foi uma utlização bem simples para este caso, aonde somente o que diferencia cada template
é somente o nome dele.

## Caso real
Na empresa que trabalho hoje, contatamos nosso cliente via email em **diversas** situações 
utilizando a API do Mandrill.

Em cada situação que tinhamos que enviar o email, nós implementávamos **todos os passos** para 
o envio do email:
- Pegar o nome do template
- Buscar os dados do cliente
- Construção do dict para o envio
- Check se o serviço do Mandrill estava online
- Envio do email

Quando tinhamos 10 templates... era... aceitável ~~nem tanto~~, mas seguimos assim.

Entretanto, após um tempo tinhas 40 templates, e cada vez mais a esteira se complicoi e sempre
era um parto pra fazer qualquer mudança em relação a email.

A solução foi fazer algo semelhante a este exemplo, onde temos uma classe principal
de envio de email (**contexto**), que dentro dela chama algumas funções que retornam os 
dados para envio do email (template, dados formatados, lista de emails) que são extraídos
de uma classe de template de email(**estratégia**).

Agora, a implementação de novos templates é super simples, e a classe de envio de email
em si nunca mais foi editada.