from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard




class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.children.append(modules.RecentActions(
            _('Acciones recientes'),
            10,
            column=1,
            order=0
        ))
        self.children.append(modules.ModelList(
            _('Modelos'),
            exclude=('auth.*',),
            column=0,
            order=0
        ))

