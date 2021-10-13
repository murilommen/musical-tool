from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from musical_tool.domain import schemas
from musical_tool.domain import actions
from musical_tool.infrastructure import context_manager

router = APIRouter()


@router.post("/analysis", status_code=status.HTTP_201_CREATED)
def create_analysis(request: schemas.AnalysisRequest, 
                    db: Session = Depends(context_manager.get_db)):
    
    new_analysis = actions.register_analysis(
        db=db,
        group=request.group,
        music=request.music,
        analysis_object=request.musicAnalysis,
        params_list=request.params,
        user_name=request.name,
    )
    return new_analysis
