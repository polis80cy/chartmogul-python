from ..api.customers.subscription import CustomerSubscription as SubsNew
from warnings import warn


class Subscription(SubsNew):
    @classmethod
    def all(cls, *args, **kwargs):
        warn("chartmogul.imp namespace is deprecated, use chartmogul.CustomerSubscription.list_imported!")
        return super(Subscription, cls).list_imported(*args, **kwargs)

    @classmethod
    def cancel(cls, *args, **kwargs):
        warn("chartmogul.imp namespace is deprecated, use chartmogul.CustomerSubscription.cancel!")
        return super(Subscription, cls).cancel(*args, **kwargs)
