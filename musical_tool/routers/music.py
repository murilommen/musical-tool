from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from musical_tool.domain import schemas
from musical_tool.domain import actions

router = APIRouter()


@router.post("/analysis", status_code=status.HTTP_201_CREATED)
def create_analysis(request: schemas.Analysis):
    actions.register_analysis(analysis_object=jsonable_encoder(request))

@router.get("/musics", status_code=status.HTTP_200_OK)
def get_musics():
    return actions.list_musics()