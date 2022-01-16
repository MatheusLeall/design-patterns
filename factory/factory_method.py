from abc import ABCMeta, abstractmethod
from cProfile import Profile
from typing import Any, List


class Section(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self: object) -> str:
        pass


class PersonalSection(Section):
    def __repr__(self: object) -> str:
        return "Personal Section"


class AlbumSection(Section):
    def __repr__(self: object) -> str:
        return "Album Section"


class ProjectSection(Section):
    def __repr__(self: object) -> str:
        return "Project Section"


class PublicationSection(Section):
    def __repr__(self: object) -> str:
        return "Publication Section"


class Profile(metaclass=ABCMeta):
    def __init__(self: object) -> None:
        self.sections: List[Any] = list()
        self.create_profile()

    @abstractmethod
    def create_profile(self: object) -> None:
        pass

    def get_sections(self: object) -> List[Any]:
        return self.sections

    def add_section(self: object, section: Section):
        self.sections.append(section)


class Linkedin(Profile):
    def create_profile(self: object):
        self.add_section(PersonalSection())
        self.add_section(ProjectSection())
        self.add_section(PublicationSection())


class Facebook(Profile):
    def create_profile(self: object):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())
        self.add_section(PublicationSection())


if __name__ == "__main__":
    supported_networks = ["Facebook", "Linkedin"]
    social_network = input("Which social network would you like to create? [Facebook, Linkedin]: ").capitalize()

    if social_network not in supported_networks:
        raise ValueError("Social network not exists!")

    profile = eval(social_network)()

    print(f"\nCreating profile on {type(profile).__name__}")
    print(f"Profile sections: {profile.get_sections()}\n")
