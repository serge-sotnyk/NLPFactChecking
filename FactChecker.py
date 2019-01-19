import csv
from FactEntityExtraction import FactEntityExtraction
from WikipediaHelper import WikipediaHelper


class FactChecker:
    def __init__(self):
        self.fact_entity_extraction = FactEntityExtraction()
        self.wikipedia_helper = WikipediaHelper()
        pass

    def check_fact(self, fact):

        # get named entities
        named_entities = self.fact_entity_extraction.extract_named_entities(fact)

        named_entities_with_pages = {}

        for entity in named_entities:
            named_entities_with_pages[entity] = self.wikipedia_helper.get_entity_wikipage_cached(entity)

        num_of_common_occurences = 0
        total_num_of_occurences = 0
        compared_entities = set()

        for subject_entity in named_entities:
            for candidate_entity in named_entities:

                subject_page = named_entities_with_pages[subject_entity]

                if subject_page is None:
                    continue

                comma_seperated_entities = subject_entity + ',' + candidate_entity
                comma_seperated_entities_reverse = candidate_entity + ',' + subject_entity

                if subject_entity != candidate_entity and not comma_seperated_entities in compared_entities:

                    # check if entities exist together
                    if candidate_entity in subject_page.content:
                        num_of_common_occurences += 1
                    
                    total_num_of_occurences += 1
                    compared_entities.add(comma_seperated_entities)
                    compared_entities.add(comma_seperated_entities_reverse)

        if total_num_of_occurences == 0:
            return 0.0

        similarity_percentage = num_of_common_occurences / total_num_of_occurences

        if similarity_percentage > 0.7:
            return 1.0
        else:
            return 0.0


if __name__ == "__main__":

    path = "train-short.tsv"

    success_count = 0.0
    num_of_rows = 0.0
    
    fact_checker = FactChecker()

    with open(path, encoding="latin-1") as tsvfile:
        next(tsvfile)
        reader = csv.reader(tsvfile, delimiter='\t')

        for row in reader:
            if len(row) < 3:
                continue

            fact = row[1]
            expected_val = float(row[2])

            estimated_val = float(fact_checker.check_fact(fact))
            print(expected_val, estimated_val)

            if expected_val == estimated_val:
                success_count += 1.0
            
            num_of_rows += 1.0
    
    print(success_count / num_of_rows)

    # extraction = FactEntityExtraction()
    # extraction.process_fact("John Sparrow David Thompson's office is Canada")