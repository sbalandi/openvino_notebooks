from typing import Callable
import gradio as gr


def make_demo(fn: Callable, quantized: bool):
    demo = gr.Interface(
        description=f"""
                    <div style="text-align: center; max-width: 700px; margin: 0 auto;">
                    <div
                        style="
                        display: grid; align-items: center; gap: 0.8rem; font-size: 1.75rem;
                        "
                    >
                        <h1 style="font-weight: 900; margin-bottom: 7px; line-height: normal;">
                            OpenVINO Generate API Whisper demo {'with quantized model.' if quantized else ''}
                        </h1>
                        <div style="font-size: 12px;">Note: 30 sec is the maximum supported audio signal for GenAI Whisper Pipeline. Longer audio can be input, but the output may be unexpected.</div>
                    </div>
                    </div>
                """,
        fn=fn,
        inputs=[
            gr.Textbox(label="YouTube URL"),
            gr.Radio(["Transcribe", "Translate"], value="Transcribe"),
            gr.Checkbox(
                value=quantized,
                visible=quantized,
                label="Use INT8",
            ),
        ],
        outputs="video",
        examples=[["https://youtu.be/kgL5LBM-hFI", "Transcribe"]],
        allow_flagging="never",
    )

    return demo
