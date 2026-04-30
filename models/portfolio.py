from pydantic import BaseModel
from typing import List, Optional
from .skills import Skill
from pydantic import Field


class Contact(BaseModel):
    email: str
    phone: str = ""
    location: str


class SocialLink(BaseModel):
    label: str
    url: str
    svg_path: Optional[str] = None
    svg_data: Optional[str] = None


class WorkExperience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: str
    summary: str
    highlights: List[str]


class ProjectImage(BaseModel):
    img_path: str
    caption: str


class Project(BaseModel):
    title: str
    summary: str
    url: Optional[str] = None
    highlights: List[str] = Field(default_factory=list)
    images: List[ProjectImage] = Field(default_factory=list)
    embed_url: Optional[str] = None


class Education(BaseModel):
    institution: str
    location: str
    degrees: List[str] = Field(default_factory=list)
    highlights: List[str] = Field(default_factory=list)
    honors: List[str] = Field(default_factory=list)
    graduation_date: Optional[str] = None


class InterestImage(BaseModel):
    img_path: str
    caption: str


class Interest(BaseModel):
    name: str
    summary: str
    images: List[InterestImage] = Field(default_factory=list)


class Portfolio(BaseModel):
    name: str
    label: str
    image_path: str

    contact: Contact
    summary: str

    social_links: List[SocialLink]
    work_experience: List[WorkExperience]
    projects: List[Project]
    education: List[Education]
    skills: List[Skill]
    interests: List[Interest]
