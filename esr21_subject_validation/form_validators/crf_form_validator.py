from django import forms
# from django.apps import apps as django_apps
# from edc_action_item.site_action_items import site_action_items
# from edc_constants.constants import NO, NEW
# from esr21_prn.action_items import CAREGIVEROFF_STUDY_ACTION


class CRFFormValidator:

    def clean(self):
        self.validate_against_visit_datetime(
            self.cleaned_data.get('report_datetime'))
        super().clean()

    def validate_against_visit_datetime(self, report_datetime):
        if (report_datetime and report_datetime <
                self.cleaned_data.get('subject_visit').report_datetime):
            raise forms.ValidationError(
                "Report datetime cannot be before visit datetime.")

    # def validate_offstudy_model(self):
        # caregiver_offstudy_cls = django_apps.get_model(
            # 'flourish_prn.caregiveroffstudy')
        # action_cls = site_action_items.get(
            # caregiver_offstudy_cls.action_name)
        # action_item_model_cls = action_cls.action_item_model_cls()
        #
        # try:
            # action_item_model_cls.objects.get(
                # subject_identifier=self.subject_identifier,
                # action_type__name=CAREGIVEROFF_STUDY_ACTION,
                # status=NEW)
        # except action_item_model_cls.DoesNotExist:
            # try:
                # caregiver_offstudy_cls.objects.get(
                    # subject_identifier=self.subject_identifier)
            # except caregiver_offstudy_cls.DoesNotExist:
                # pass
            # else:
                # raise forms.ValidationError(
                    # 'Participant has been taken offstudy. Cannot capture any '
                    # 'new data.')
        # else:
            # self.subject_visit = self.cleaned_data.get('subject_visit') or None
            # if not self.subject_visit or self.subject_visit.require_crfs == NO:
                # raise forms.ValidationError(
                    # 'Participant is scheduled to be taken offstudy without '
                    # 'any new data collection. Cannot capture any new data.')
