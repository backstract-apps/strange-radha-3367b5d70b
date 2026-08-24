from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class DndGhostTable(BaseModel):
    person_name: Optional[str]=None
    person_role: Optional[str]=None
    company_name: Optional[str]=None
    company_email: Optional[str]=None
    role_hired_for: Optional[str]=None
    city: Optional[str]=None
    industry: Optional[str]=None
    estimated_cost: Optional[str]=None
    days_lost: Optional[str]=None
    process_breakdown: Optional[str]=None
    timeline_files: Optional[Dict]=None


class ReadDndGhostTable(BaseModel):
    person_name: Optional[str]=None
    person_role: Optional[str]=None
    company_name: Optional[str]=None
    company_email: Optional[str]=None
    role_hired_for: Optional[str]=None
    city: Optional[str]=None
    industry: Optional[str]=None
    estimated_cost: Optional[str]=None
    days_lost: Optional[str]=None
    process_breakdown: Optional[str]=None
    timeline_files: Optional[Dict]=None
    class Config:
        from_attributes = True


class MaysonPlatformAuth(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    is_verified: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadMaysonPlatformAuth(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    is_verified: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class MaysonPlatformAuthMagicLink(BaseModel):
    email: Optional[str]=None
    token_hash: Optional[str]=None
    is_used: Optional[bool]=None
    expires_at: Optional[datetime.time]=None
    created_at: Optional[datetime.time]=None


class ReadMaysonPlatformAuthMagicLink(BaseModel):
    email: Optional[str]=None
    token_hash: Optional[str]=None
    is_used: Optional[bool]=None
    expires_at: Optional[datetime.time]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class MaysonPlatformAuthOtp(BaseModel):
    email: Optional[str]=None
    otp: Optional[str]=None
    validity: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadMaysonPlatformAuthOtp(BaseModel):
    email: Optional[str]=None
    otp: Optional[str]=None
    validity: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class MaysonRequestLogger(BaseModel):
    ts_utc: Optional[datetime.time]=None
    method: Optional[str]=None
    path: Optional[str]=None
    status_code: Optional[Union[int, float]]=None
    duration_ms: Optional[float]=None
    client_ip: Optional[str]=None
    user_agent: Optional[str]=None
    content_length: Optional[Union[int, float]]=None
    query_params: Optional[str]=None
    style: Optional[str]=None
    message: Optional[str]=None


class ReadMaysonRequestLogger(BaseModel):
    ts_utc: Optional[datetime.time]=None
    method: Optional[str]=None
    path: Optional[str]=None
    status_code: Optional[Union[int, float]]=None
    duration_ms: Optional[float]=None
    client_ip: Optional[str]=None
    user_agent: Optional[str]=None
    content_length: Optional[Union[int, float]]=None
    query_params: Optional[str]=None
    style: Optional[str]=None
    message: Optional[str]=None
    class Config:
        from_attributes = True


class NotionUsers(BaseModel):
    email: Optional[str]=None
    notion_user_id: Optional[str]=None
    notion_access_token: Optional[str]=None
    notion_workspace_id: Optional[str]=None
    notion_workspace_name: Optional[str]=None
    notion_workspace_icon: Optional[str]=None
    notion_connected_at: Optional[datetime.time]=None
    created_at: Optional[datetime.time]=None
    updated_at: Optional[datetime.time]=None


class ReadNotionUsers(BaseModel):
    email: Optional[str]=None
    notion_user_id: Optional[str]=None
    notion_access_token: Optional[str]=None
    notion_workspace_id: Optional[str]=None
    notion_workspace_name: Optional[str]=None
    notion_workspace_icon: Optional[str]=None
    notion_connected_at: Optional[datetime.time]=None
    created_at: Optional[datetime.time]=None
    updated_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    email: str
    password: str
    phone: Optional[str]=None
    created_at: Optional[datetime.time]=None
    notion_user_id: Optional[str]=None
    notion_access_token: Optional[str]=None
    notion_workspace_id: Optional[str]=None
    notion_workspace_name: Optional[str]=None
    notion_workspace_icon: Optional[str]=None
    notion_connected_at: Optional[datetime.time]=None


class ReadUsers(BaseModel):
    email: str
    password: str
    phone: Optional[str]=None
    created_at: Optional[datetime.time]=None
    notion_user_id: Optional[str]=None
    notion_access_token: Optional[str]=None
    notion_workspace_id: Optional[str]=None
    notion_workspace_name: Optional[str]=None
    notion_workspace_icon: Optional[str]=None
    notion_connected_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    phone: Optional[str]=None
    created_at: Optional[Any]=None
    notion_user_id: Optional[str]=None
    notion_access_token: Optional[str]=None
    notion_workspace_id: Optional[str]=None
    notion_workspace_name: Optional[str]=None
    notion_workspace_icon: Optional[str]=None
    notion_connected_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutUsersUserId(BaseModel):
    user_id: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)
    phone: Optional[str]=None
    created_at: Optional[Any]=None
    notion_user_id: Optional[str]=None
    notion_access_token: Optional[str]=None
    notion_workspace_id: Optional[str]=None
    notion_workspace_name: Optional[str]=None
    notion_workspace_icon: Optional[str]=None
    notion_connected_at: Optional[Any]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetUsersUserIdQueryParams(BaseModel):
    """Query parameter validation for get_users_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True


class DeleteUsersUserIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True
