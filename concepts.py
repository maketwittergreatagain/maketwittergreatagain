# coding=utf-8
import json
import time
from watson_developer_cloud import ConceptExpansionV1Beta as ConceptExpansion
import secret
import json
concept_expansion = ConceptExpansion(username=secret.WATSON_USERNAME,
                                     password=secret.WATSON_PASSWORD)

#seed = "sports"


def getConcepts(seed):
    job_id = concept_expansion.create_job(dataset='mtsamples', seeds=[seed]) 
    #print(json.dumps(job_id, indent=2))

    time.sleep(1)  # sleep for 5 seconds
    job_status = concept_expansion.get_status(job_id)

    while job_status['status'] == 'in progress' or job_status['status'] == 'awaiting work':
        time.sleep(1)  # sleep for 5 seconds
        job_status = concept_expansion.get_status(job_id)
        print(json.dumps(job_status, indent=2))

    if job_status['status'] == 'done':
        new_html = []
        results = concept_expansion.get_results(job_id)
        #print(json.dumps(results, indent=2))
        json_dict = json.loads(json.dumps(results))
        for domain_dict in json_dict['return_seeds']:
            new_html.append(domain_dict['result']) #+= "%s\n" % domain_dict['result']
        return new_html

#getConcepts(seed)
