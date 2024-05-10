# generated by datamodel-codegen:
#   filename:  dataplane.yaml

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import ConfigDict, Field, RootModel

from .base import BaseModel


class MetadataServerResponse(BaseModel):
    name: str
    version: str
    extensions: List[str]


class MetadataServerErrorResponse(BaseModel):
    error: str


class MetadataModelErrorResponse(BaseModel):
    error: str


class Parameters(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    content_type: Optional[str] = None
    headers: Optional[Dict[str, Any]] = None


class TensorData(RootModel[Union[List, str]]):
    root: Union[List, str] = Field(..., title="TensorData")

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, idx):
        return self.root[idx]

    def __len__(self):
        return len(self.root)


class RequestOutput(BaseModel):
    name: str
    parameters: Optional[Parameters] = None


class InferenceErrorResponse(BaseModel):
    error: Optional[str] = None


class Datatype(Enum):
    BOOL = "BOOL"
    UINT8 = "UINT8"
    UINT16 = "UINT16"
    UINT32 = "UINT32"
    UINT64 = "UINT64"
    INT8 = "INT8"
    INT16 = "INT16"
    INT32 = "INT32"
    INT64 = "INT64"
    FP16 = "FP16"
    FP32 = "FP32"
    FP64 = "FP64"
    BYTES = "BYTES"


class MetadataTensor(BaseModel):
    name: str
    datatype: Datatype
    shape: List[int]
    parameters: Optional[Parameters] = None


class RequestInput(BaseModel):
    name: str
    shape: List[int]
    datatype: Datatype
    parameters: Optional[Parameters] = None
    data: TensorData


class ResponseOutput(BaseModel):
    name: str
    shape: List[int]
    datatype: Datatype
    parameters: Optional[Parameters] = None
    data: TensorData


class InferenceResponse(BaseModel):
    model_name: str
    model_version: Optional[str] = None
    id: Optional[str] = None
    parameters: Optional[Parameters] = None
    outputs: List[ResponseOutput]


class MetadataModelResponse(BaseModel):
    name: str
    versions: Optional[List[str]] = None
    platform: str
    inputs: Optional[List[MetadataTensor]] = None
    outputs: Optional[List[MetadataTensor]] = None
    parameters: Optional[Parameters] = None


class InferenceRequest(BaseModel):
    id: Optional[str] = None
    parameters: Optional[Parameters] = None
    inputs: List[RequestInput]
    outputs: Optional[List[RequestOutput]] = None
