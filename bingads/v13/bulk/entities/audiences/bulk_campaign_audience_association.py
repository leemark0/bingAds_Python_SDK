from bingads.v13.bulk.entities import *
from bingads.service_client import _CAMPAIGN_OBJECT_FACTORY_V13
from bingads.v13.bulk.entities.target_criterions.bulk_campaign_biddable_criterion import BulkCampaignBiddableCriterion
from bingads.v13.internal.bulk.mappings import _SimpleBulkMapping
from bingads.v13.internal.bulk.string_table import _StringTable
from bingads.v13.internal.extensions import *


class BulkCampaignAudienceAssociation(BulkCampaignBiddableCriterion):
    """ Base class for all Campaign Audience Association subclasses that can be read or written in a bulk file.

    *See also:*

    * :class:`.BulkCampaignCustomAudienceAssociation`
    * :class:`.BulkCampaignInMarketAudienceAssociation`
    * :class:`.BulkCampaignProductAudienceAssociation`
    * :class:`.BulkCampaignRemarketingListAssociation`
    * :class:`.BulkCampaignSimilarRemarketingListAssociation`
    """

    def __init__(self,
                 biddable_campaign_criterion=None,
                 campaign_name=None,
                 audience_name=None):
        super(BulkCampaignAudienceAssociation, self).__init__(biddable_campaign_criterion, campaign_name)

        self._audience_name = audience_name
        self._performance_data = None

    _MAPPINGS = [
        _SimpleBulkMapping(
            _StringTable.Audience,
            field_to_csv=lambda c: c.audience_name,
            csv_to_field=lambda c, v: setattr(c, 'audience_name', v)
        ),
        _SimpleBulkMapping(
            _StringTable.BidAdjustment,
            field_to_csv=lambda c: field_to_csv_BidAdjustment(c.biddable_campaign_criterion),
            csv_to_field=lambda c, v: csv_to_field_BidAdjustment(c.biddable_campaign_criterion, float(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.AudienceId,
            field_to_csv=lambda c: field_to_csv_CriterionAudienceId(c.biddable_campaign_criterion),
            csv_to_field=lambda c, v: csv_to_field_CriterionAudienceId(c.biddable_campaign_criterion, int(v) if v else None)
        ),
    ]

    @property
    def audience_name(self):
        """ Defines the name of the Audience

        :rtype: str
        """

        return self._audience_name

    @audience_name.setter
    def audience_name(self, audience_name):
        self._audience_name = audience_name
        
        
    def create_criterion(self):
        self._biddable_campaign_criterion.Criterion = _CAMPAIGN_OBJECT_FACTORY_V13.create('AudienceCriterion')
        self._biddable_campaign_criterion.Criterion.Type = 'AudienceCriterion'

    def process_mappings_from_row_values(self, row_values):
        super(BulkCampaignAudienceAssociation, self).process_mappings_from_row_values(row_values)
        row_values.convert_to_entity(self, BulkCampaignAudienceAssociation._MAPPINGS)

    def process_mappings_to_row_values(self, row_values, exclude_readonly_data):
        super(BulkCampaignAudienceAssociation, self).process_mappings_to_row_values(row_values, exclude_readonly_data)
        self.convert_to_values(row_values, BulkCampaignAudienceAssociation._MAPPINGS)
    
    def read_additional_data(self, stream_reader):
        super(BulkCampaignAudienceAssociation, self).read_additional_data(stream_reader)
