import argparse
from questiongenerator import QuestionGenerator
from questiongenerator import print_jsn
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_restful import reqparse, Resource
import json

__all__ =('QuesMcq')

class QuesMcq(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("count", type=int,default=10)
        parser.add_argument('text', type=str, help='text is required')
        parser.add_argument("--show_answers", dest="show_answers", action="store_true", default=True)
        parser.add_argument("style",default="multiple_choice", type=str)  ## help="The desired type of answers. Choose from ['all', 'sentences', 'multiple_choice']"
        args = parser.parse_args()

        try:            
            if args.text is None or args.text == '' : 
                    return {
                            "Result": False,
                            "Message":"text is required"}, 400

            if args.count is None or args.count == '' : 
                    return {
                            "Result": False,
                            "Message":"num_questions is required"}, 400

           
            text = args.text
            qg = QuestionGenerator()
            qa_list = qg.generate(text,answer_style=args.style,num_questions=int(args.count))
            return {"Result":True, "Data":print_jsn(qa_list, data = text)}
            
        except BaseException as excep:
            return { "Result": False, "Message":str(excep)}, 500
