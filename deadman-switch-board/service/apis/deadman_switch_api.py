import time

INTERVALS = [1, 60, 3600, 86400, 604800, 2419200, 29030400]
NAMES = [('second', 'seconds'),
        ('minute', 'minutes'),
        ('hour', 'hours'),
        ('day', 'days'),
        ('week', 'weeks'),
        ('month', 'months'),
        ('year', 'years')]


class DeadmanSwitch():
    def on_post(req, resp, *, name, frequency, token):
        """update switch with check-in info"""
        time_now = time.time()
        # validate token
        # validate if named switch exists or not for team, based upon token

    def on_get(self, req, resp, *, name, token):
        """get switch details"""
        

    def _get_future_epoch_from_input(self, amount, units):
        """
        Divide `amount` in time periods.
        Useful for making time intervals more human readable.

        Need to refactor to just return EPOCH of time in future

        >>> humanize_input(173, 'hours')
        [(1, 'week'), (5, 'hours')]
        >>> humanize_input(17313, 'seconds')
        [(4, 'hours'), (48, 'minutes'), (33, 'seconds')]
        >>> humanize_input(90, 'weeks')
        [(1, 'year'), (10, 'months'), (2, 'weeks')]
        >>> humanize_input(42, 'months')
        [(3, 'years'), (6, 'months')]
        >>> humanize_input(500, 'days')
        [(1, 'year'), (5, 'months'), (3, 'weeks'), (3, 'days')]
        """
        result = []

        unit = map(lambda a: a[1], NAMES).index(units)
        # Convert user input
        amount = amount * INTERVALS[unit]

        future_epoch = time.time() + amount
        return result


class DeadmanSwitchHealth():
    async def greet_world(req, resp):
        resp.text = f"host healthy"
