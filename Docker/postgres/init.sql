CREATE database IF NOT EXISTS wapico;
CREATE user IF NOT EXISTS wapico with password 'wapico';
ALTER database wapico owner to wapico;