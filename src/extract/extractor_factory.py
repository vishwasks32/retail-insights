# Factory for extractors
class ExtractorFactory:
    def get_extractor(self, source_type):
        if source_type == 'csv':
            from .csv_extractor import CSVExtractor
            return CSVExtractor()
        elif source_type == 'api':
            from .api_extractor import APIExtractor
            return APIExtractor()
        elif source_type == 'db':
            from .db_extractor import DBExtractor
            return DBExtractor()
        else:
            raise ValueError('Unknown source type')
