from prometheus_client import  Counter, Gauge

oplog_lag_in_seconds = Gauge('oplog_lag_in_seconds', 'oplog lag', ['source', 'target'])
transferred_rows = Counter('transferred_rows', 'how many rows has been transferred', ['source', 'target'])
total_rows = Gauge('total_rows', 'total rows to be transferred', ['source', 'target'])

_lables = []