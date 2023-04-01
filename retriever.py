

def get_relevant_docs(claim_number):
    context = """
    IBCC for claim no AJSYC1100019
    CM has been assigned
    Customer is not happy since the roof is not repaired properly.

    access amount 1500$
    CM yasmin will contact customer

    Next Actions:
    - CM to call customer
    - Plan repairs
    - Check coverage
    """

    if claim_number == 'AJSYC1100019':
        return context
    else:
        return 'No information found for claim number.'


