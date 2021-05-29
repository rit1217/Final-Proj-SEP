from databasemodel.modelConstant import *

class CommentModel:
    def __init__( self ):
        pass

    def insertComment( self, username, recipe_id, comment ):
        CURSOR.execute( "INSERT INTO Comment(USERNAME, RECIPE_ID, COMMENT) VALUES(?,?,?)", (username, recipe_id, comment))
        CONNECTION.commit()

    def getCommentByRecipe( self, recipe_id ):
        statement = "SELECT USERNAME, COMMENT FROM Comment WHERE RECIPE_ID = '%s'" %(recipe_id)
        CURSOR.execute( statement )
        result = CURSOR.fetchall()
        CONNECTION.commit()
        return result

COMMENT_MODEL = CommentModel()