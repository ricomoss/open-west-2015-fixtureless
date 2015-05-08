from django.views.generic import View
from django.shortcuts import render

from owc_fixtureless.models import Mage
from owc_fixtureless import constants


class MageView(View):
    template = 'mage_template.html'

    def _get_context(self, mages):
        if mages.count() <= constants.HIGH_DETAIL_COUNT_LIMIT:
            return self._high_details(mages)
        elif mages.count() <= constants.MEDIUM_DETAIL_COUNT_LIMIT:
            return self._medium_details(mages)
        return self._low_details(mages)

    def _high_details(self, mages):
        context = list()
        for mage in mages:
            mage_dict = {
                'name': mage.name,
                'magic_type': mage.magic_type,
            }
            if mage.unicorn_set.all().exists():
                mage_dict['friends'] = [
                    unicorn.details for unicorn in mage.unicorn_set.all()
                ]
            context.append(mage_dict)
        return context

    def _medium_details(self, mages):
        context = list()
        for mage in mages:
            context.append({
                'name': mage.name,
                'magic_type': mage.magic_type,
            })
        return context

    def _low_details(self, mages):
        context = list()
        for mage in mages:
            context.append({
                'name': mage.name,
            })
        return context

    def get(self, request):
        mages = Mage.objects.all()
        context = {'data': self._get_context(mages)}
        return render(request, self.template, context)
