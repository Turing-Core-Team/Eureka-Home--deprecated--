class OpportunitiesResponse:
    tags: str
    link: str
    title: str
    requirements: str
    awards: str
    description: str
    publication_date: str
    update_date: str
    due_date: str


def __init__(self,
             tags: str,
             link: str,
             title: str,
             requirements: str,
             awards: str,
             description: str,
             publication_date: str,
             update_date: str,
             due_date: str):
    self.tags = tags
    self.link = link
    self.title = title
    self.requirements = requirements
    self.awards = awards
    self.description = description
    self.publication_date = publication_date
    self.update_date = update_date
    self.due_date = due_date
