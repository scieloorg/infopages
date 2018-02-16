import colander


# SciELO
class OtherIssns(colander.SequenceSchema):
    other_issn = colander.SchemaNode(colander.String())


class Title(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    initial_year = colander.SchemaNode(colander.String())
    final_year = colander.SchemaNode(colander.String())


class PreviousTitle(colander.MappingSchema):
    previous_title = colander.SchemaNode(colander.String())
    initial_year = colander.SchemaNode(colander.String())
    final_year = colander.SchemaNode(colander.String())


class NextTitle(colander.MappingSchema):
    next_title = colander.SchemaNode(colander.String())
    initial_year = colander.SchemaNode(colander.String())
    final_year = colander.SchemaNode(colander.String())


class AbstractLanguages(colander.SequenceSchema):
    abstract_languages = colander.SchemaNode(colander.String())


class ControlledVocabulary(colander.TupleSchema):
    vocabulary = colander.SchemaNode(colander.String())
    descriptor = colander.SchemaNode(colander.String())


class EditorialStandard(colander.TupleSchema):
    standard = colander.SchemaNode(colander.String())
    descriptor = colander.SchemaNode(colander.String())


class IndexCoverage(colander.SequenceSchema):
    index_coverage = colander.NoneAcceptantNode(colander.String())


class WosIndexes(colander.SequenceSchema):
    wos_citation_index = colander.SchemaNode(colander.String())


class WosSubjectsAreas(colander.SequenceSchema):
    wos_subject_area = colander.SchemaNode(colander.String())


class Languages(colander.SequenceSchema):
    language = colander.SchemaNode(colander.String())


class Mission(colander.MappingSchema):
    pt = colander.SchemaNode(colander.String())
    es = colander.SchemaNode(colander.String())
    en = colander.SchemaNode(colander.String())


class Periodicity(colander.TupleSchema):
    periodicity_acronym = colander.SchemaNode(colander.String())
    descriptor = colander.SchemaNode(colander.String())


class Permissions(colander.MappingSchema):
    id = colander.SchemaNode(colander.String())
    url = colander.SchemaNode(colander.url())
    text = colander.SchemaNode(colander.String())


class PublisherCountry(colander.TupleSchema):
    country_iso = colander.SchemaNode(colander.String())
    country_name = colander.SchemaNode(colander.String())


class PublisherName(colander.SequenceSchema):
    publisher_name = colander.SchemaNode(colander.String())


class Sponsors(colander.SequenceSchema):
    sponsor = colander.SchemaNode(colander.String())


class SubjectAreas(colander.SequenceSchema):
    subject_area = colander.SchemaNode(colander.String())


class DoiProvider(colander.MappingSchema):
    prefix = colander.SchemaNode(colander.String())
    publisher = colander.SchemaNode(colander.String())


class DoajApc(colander.MappingSchema):
    currency = colander.SchemaNode(colander.String())
    average_price = colander.SchemaNode(colander.Int())


class DoajAuthorCopyright(colander.MappingSchema):
    copyright = colander.SchemaNode(colander.Boolean())
    url = colander.SchemaNode(colander.url())


class DoajAuthorPublishingRights(colander.MappingSchema):
    publishing_rights = colander.SchemaNode(colander.Boolean())
    url = colander.SchemaNode(colander.url())


class DoajDepositPolicy(colander.SequenceSchema):
    deposit_policy = colander.SchemaNode(colander.String())


class DoajEditorialReview(colander.MappingSchema):
    process = colander.SchemaNode(colander.String())
    url = colander.SchemaNode(colander.url())


class DoajPlagiarismDetection(colander.MappingSchema):
    detection = colander.SchemaNode(colander.Boolean())
    url = colander.SchemaNode(colander.url())


class DoajSubmissionsCharges(colander.MappingSchema):
    currency = colander.SchemaNode(colander.String())
    average_price = colander.SchemaNode(colander.Int())


class Doaj(colander.MappingSchema):
    apc = colander.SchemaNode(colander.url())
    author_copyright = DoajAuthorCopyright()
    author_pays = colander.SchemaNode(
        colander.String(),
        validator=colander.OneOf(['N', 'NY']))
    author_pays_url = colander.SchemaNode(colander.url())
    author_publishing_rights = DoajAuthorPublishingRights()
    deposit_policy = DoajDepositPolicy()
    editorial_review = DoajEditorialReview()
    plagiarism_detection = DoajPlagiarismDetection()
    query_url = colander.SchemaNode(colander.url())
    submissions_charges = DoajSubmissionsCharges()
    submissions_charges_url = colander.SchemaNode(colander.url())


class Journal(colander.MappingSchema):
    scielo_issn = colander.SchemaNode(colander.String())
    print_issn = colander.SchemaNode(colander.String())
    electronic_issn = colander.SchemaNode(colander.String())
    other_issns = OtherIssns()
    title = Title()
    fulltitle = colander.SchemaNode(colander.String())
    previous_title = PreviousTitle()
    next_title = NextTitle()
    title_nlm = colander.SchemaNode(colander.String())
    abbreviated_iso_title = colander.SchemaNode(colander.String())
    abbreviated_issn_title = colander.SchemaNode(colander.String())
    abstract_languages = AbstractLanguages()
    acronym = colander.SchemaNode(colander.String())
    collection_acronym = colander.SchemaNode(colander.String())
    controlled_vocabulary = ControlledVocabulary()
    copyright = colander.SchemaNode(colander.String())
    creation_date = colander.SchemaNode(colander.Date)
    current_status = colander.SchemaNode(colander.String())
    journal_email = colander.SchemaNode(colander.Email())
    name_of_chief_editor = colander.SchemaNode(colander.String())
    email_of_chief_editor = colander.SchemaNode(colander.Email())
    editorial_standard = EditorialStandard()
    first_number = colander.NoneAcceptantNode(colander.Int())
    first_volume = colander.NoneAcceptantNode(colander.Int())
    first_year = colander.NoneAcceptantNode(colander.Int())
    index_coverage = IndexCoverage()
    wos_citations_indexes = WosIndexes()
    wos_subjects_areas = WosSubjectsAreas()
    is_indexed_in_scopus = colander.SchemaNode(colander.Boolean())
    is_indexed_in_pubmed = colander.SchemaNode(colander.Boolean())
    is_indexed_in_pmc = colander.SchemaNode(colander.Boolean())
    is_indexed_in_google_scholar = colander.SchemaNode(colander.Boolean())

    # Instructions to autors
    accepts_preprint = colander.SchemaNode(colander.Boolean())
    guides_data_referencing = colander.SchemaNode(colander.Boolean())
    apc_charges = colander.SchemaNode(colander.Boolean())
    apc_valeu1 = colander.SchemaNode(colander.Float())
    apc_value2 = colander.SchemaNode(colander.Float())

    is_publishing_model_continuous = colander.SchemaNode(colander.Boolean())
    languages = Languages()
    mission = Mission()
    periodicity = Periodicity()
    periodicity_in_months = colander.SchemaNode(
        colander.Int(),
        validator=colander.Range(1, 12))  # undefined ?
    permissions = Permissions()
    publisher_city = colander.SchemaNode(colander.String())
    publisher_country = PublisherCountry()
    publisher_address = colander.SchemaNode(colander.String())
    publisher_name = PublisherName()
    publisher_state = colander.SchemaNode(colander.String())
    publisher_model = colander.SchemaNode(
        colander.String,
        validator=colander.OneOf(['regular', 'continuos']))
    scimago_code = colander.NoneAcceptantNode(colander.String())
    sponsors = Sponsors()
    subject_areas = SubjectAreas()
    submission_url = colander.NoneAcceptantNode(colander.url())
    doi_provider = DoiProvider()

    # DOAJ
    doaj = Doaj()
