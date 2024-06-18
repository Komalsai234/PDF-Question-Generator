prompt = """

You are a expert in creating interview question based upon on the give documentation and content.
The main goal on which you are appointed is to create a high level question which are helpful in the preparation.
Here is the content on which you should create the question as mentioned above:

------------------------
{text}
------------------------

Create only meaningful and related question which helps the user in the preparation for the exam or interview
Beware that you are not missing any useful information.

Questions:

"""


refined_prompt = """
You are a expert in creating interview question based upon on the give documentation and content.
The main goal on which you are appointed is to create a high level question which are helpful in the preparation.
I have recieved some question to certain extent: {exsisting_answer}.

You have an option to refine the exsisting questions and add more if needed only.
Don't add unnecessary information, add only if required.

----------------------
{text}
----------------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the original questions.

Questions:

"""