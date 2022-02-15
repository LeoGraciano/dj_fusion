import uuid
from stdimage import StdImageField
from django.utils.translation import gettext as _
from django.db import models
from uuid import uuid4
# Create your models here.


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4}.{ext}'
    return filename


class BaseModel(models.Model):

    code = models.UUIDField(
        "code", primary_key=True, editable=False,
        unique=True, default=uuid4
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


ICON_CHOICES = (
    ('lni-cog', "Engrenagem"),
    ('lni-stats-up', "Gráfico"),
    ('lni-users', "Usuários"),
    ('lni-layers', "Design"),
    ('lni-mobile', "Mobile"),
    ('lni-rocket', "Foguete"),
    ('lni-laptop-phone', 'Note e Mobile'),
    ('lni-leaf', 'Folha'),
)


class Service(BaseModel):

    name = models.CharField(_("Serviço"), max_length=100)
    description = models.TextField(_("Descrição"), max_length=250)
    icon = models.CharField(_("Ícone"), max_length=20, choices=ICON_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Serviço")
        verbose_name_plural = _("Serviços")


class Role(BaseModel):
    role = models.CharField(_("Cargo"), max_length=100)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = _("Cargo")
        verbose_name_plural = _("Cargos")


class Employee(BaseModel):
    name = models.CharField(_("Nome"), max_length=150)
    cargo = models.ForeignKey(
        Role, related_name="employee_related", on_delete=models.SET_NULL,
        null=True
    )
    bio = models.TextField(_("Bio"), max_length=255)

    imagem = StdImageField(
        'Imagem', upload_to="employee", variations={
            'thumb': {"width": 480, "height": 480}}
    )

    facebook = models.CharField(_("Facebook"), max_length=150, default="#")
    instagram = models.CharField(_("Instagram"), max_length=150, default="#")
    twitter = models.CharField(_("Twitter"), max_length=150, default="#")

    def __str__(self):
        return f'{self.name} - {self.cargo}'

    class Meta:
        verbose_name = _("Funcionário")
        verbose_name_plural = _("Funcionários")


class Feature(BaseModel):

    name = models.CharField(_("recursos"), max_length=100)
    description = models.TextField(_("Descrição"), max_length=250)
    icon = models.CharField(_("Ícone"), max_length=20, choices=ICON_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Recurso utilizado")
        verbose_name_plural = _("Recursos utilizados")
