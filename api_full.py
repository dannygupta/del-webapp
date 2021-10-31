from flask import Flask
from flask_restful import Resource, Api, reqparse
import markdown
import markdown.extensions.fenced_code


app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string


class Classify(Resource):
    def get(self):
        post_string = "Please do a POST with your string as \"input\" parameter"
        return post_string

    
    def string_out(self, input):
        if 'Google' in input:
            return input.replace("Google","Google\u00a9")
        if 'Oracle' in input:
            return input.replace("Oracle","Oracle\u00a9")
        if 'Microsoft' in input:
            return input.replace("Microsoft","Microsoft\u00a9")
        if 'Amazon' in input:
            return input.replace("Amazon","Amazon\u00a9")
        if 'Deloitte' in input:
            return input.replace("Deloitte","Deloitte\u00a9")
        else:
            return input

    def post(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('input', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        output = self.string_out(args['input'])
        return output
        #return self.string_out(args['input'])
        #return args['input']
        #break down the string


    
#add an endpoint where we can send data
api.add_resource(Classify, '/classify')

if __name__ == '__main__':
    app.run()  # run the application 