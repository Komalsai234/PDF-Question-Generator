from src.preprocessing import file_preprocessing
from src.llm_model import llm_model
from src.prompt import prompt,refined_prompt
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain


def llm_pipeline(file_path):

    document_chunks = file_preprocessing(file_path)

    main_prompt = PromptTemplate(template=prompt,input_variables=['text'])

    refined_main_prompt = PromptTemplate(template=refined_prompt)

    question_gen_chain = load_summarize_chain(
        llm= llm_model,
        chain_type='refine',
        uestion_prompt=main_prompt, 
        refine_prompt=refined_main_prompt
    )

    generatred_questions = question_gen_chain.run(document_chunks)

    generatred_questions_list = generatred_questions.split("\n")
    filtered_generated_question_list = [element for element in generatred_questions_list if element.endswith('?') or element.endswith('.')]

    return filtered_generated_question_list