'''

Copyright (C) 2019 张珏敏.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.username: self.username = self.email.split('@')[0]
        super(User, self).save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        ordering = ['-date_joined']
        pass
