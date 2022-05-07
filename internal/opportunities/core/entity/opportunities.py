from dataclasses import dataclass


@dataclass(frozen=True)
class Opportunities:
    tags: str
    link: str
    title: str
    requirements: str
    awards: str
    description: str
    publication_date: str
    update_date: str
    due_date: str
