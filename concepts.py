# coding=utf-8
import json
import time
from watson_developer_cloud import ConceptExpansionV1Beta as ConceptExpansion
import secret

concept_expansion = ConceptExpansion(username=secret.WATSON_USERNAME,
                                     password=secret.WATSON_PASSWORD)

#seed = "sports"

def getConcepts(seed):
    job_id = concept_expansion.create_job(dataset='mtsamples', seeds=[seed]) #, label='medications')
    print(json.dumps(job_id, indent=2))

    time.sleep(5)  # sleep for 5 seconds
    job_status = concept_expansion.get_status(job_id)

    while job_status['status'] == 'in progress' or job_status['status'] == 'awaiting work':
        time.sleep(5)  # sleep for 5 seconds
        job_status = concept_expansion.get_status(job_id)
        print(json.dumps(job_status, indent=2))

    if job_status['status'] == 'done':
        results = concept_expansion.get_results(job_id)
        print(json.dumps(results, indent=2))

#getConcepts(seed)
