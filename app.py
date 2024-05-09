from transformers import pipeline
import gradio as gr

pipe = pipeline('text-generation', model='prithivMLmods/Stark-Prompt-Extender')

def extend_prompt(prompt):
    return pipe(prompt+',', num_return_sequences=1)[0]["generated_text"]

examples = [
            ['a carnival of robots in a neon cityscape'],
            ["a mermaid playing electric guitar underwater"],
            ['a swarm of fireflies illuminating a moonlit forest'],
            ["a time-traveling pirate ship sailing through a storm of stars"],
            ["a mystical portal hidden in a waterfall"],
            ]

iface = gr.Interface(
    description = "Enter a main idea for a prompt, and the model will attempt to add suitable style cues.",
    article = "<p style='text-align: center'><a href='https://github.com/PRITHIVSAKTHIUR/Prompt-Extender-Gpt' target='_blank'>🫙🪶</a></p>",
    fn=extend_prompt, 
    inputs=gr.Text(label="Type the prompt here"), 
    outputs=gr.TextArea(label='Extended prompt'),
    examples=examples,
    title="Prompt Extender"
    )

iface.launch()
