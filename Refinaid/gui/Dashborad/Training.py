# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import gradio as gr
from Refinaid.gui.Information import PageContent
from typing import Any

class TrainingComponent:

    data_summary = None
    model_dropdown = None
    dtc_criterion_dd = None
    dtc_max_depth_tb = None
    dtc_min_samples_split_sldr = None
    dtc_min_samples_leaf_sldr = None
    dtc_max_features_dd = None
    dtc_max_leaf_nodes_tb = None
    knc_n_nbr_sldr = None
    knc_weights_dd = None
    knc_althm_dd = None
    train_btn = None
    train_df = None
    train_img1 = None
    train_img2 = None
    train_img3 = None

    def __init__(self, page_content: PageContent) -> None:
        self.page_content = page_content

    def get_training(self, ):
        gr.Markdown(f"{self.page_content.explanatory_text['training']['title']}\n{self.page_content.explanatory_text['training']['body']}")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Data You have picked!!!")
                self.data_summary = gr.DataFrame(
                    headers=[
                        "Parameters",
                        "Value"
                    ],
                    row_count=(7, "fixed"),
                    col_count=(2, "fixed"),
                    interactive=False,
                )
            with gr.Column():
                self.model_dropdown = gr.Dropdown(label="Select Model", choices=self.page_content.dropdown_options["models"], interactive=True)
                # decision_tree_classifier
                self.dtc_criterion_dd = gr.Dropdown(label="Criterion", 
                                            choices=self.page_content.dropdown_options["model_parameters"]["decision_tree_classifier"]["criterion"], value="gini", interactive=True, visible=False)
                self.dtc_max_depth_tb = gr.Textbox(label="Max Depth", value="None", interactive=True, visible=False)
                self.dtc_min_samples_split_sldr = gr.Slider(label="Minimum Samples Split", minimum=2, maximum=20, step=1, value=2, interactive=True, visible=False)
                self.dtc_min_samples_leaf_sldr = gr.Slider(label="Minimum Samples Leaf", minimum=1, maximum=20, step=1, value=1, interactive=True, visible=False)
                self.dtc_max_features_dd = gr.Dropdown(label="Max Features", 
                                                choices=self.page_content.dropdown_options["model_parameters"]["decision_tree_classifier"]["max_features"], value="None", interactive=True, visible=False)
                self.dtc_max_leaf_nodes_tb = gr.Textbox(
                    label="Max Leaf Nodes", 
                    value="None", 
                    interactive=True, 
                    visible=False
                )
                
                # k_neighbors_classifier
                self.knc_n_nbr_sldr = gr.Slider(
                    label="N Neighbors", 
                    value=5, 
                    interactive=True, 
                    minimum=1, 
                    maximum=20, 
                    step=1, 
                    visible=False
                )
                self.knc_weights_dd = gr.Dropdown(
                    label="Weights", 
                    choices=self.page_content.dropdown_options["model_parameters"]["k_neighbors_classifier"]["weights"], 
                    value="uniform", 
                    interactive=True, 
                    visible=False
                )
                self.knc_althm_dd = gr.Dropdown(
                    label="Algorithm", 
                    choices=self.page_content.dropdown_options["model_parameters"]["k_neighbors_classifier"]["algorithm"], 
                    value="auto", 
                    interactive=True, 
                    visible=False
                )

        with gr.Row():
            self.train_btn = gr.Button(
                value="Train"
            )
        with gr.Row():
            gr.Markdown("## Training Result")
        with gr.Row():
            self.train_df = gr.DataFrame(
                headers=["Accuracy", "Recall", "Precision", "F1"], 
                interactive=True, 
                row_count=(1, "fixed"), 
                col_count=(4, "fixed")
            )

        with gr.Row():
            self.train_img1 = gr.Plot(interactive=True)
            self.train_img2 = gr.Plot(interactive=True)
            self.train_img3 = gr.Plot(interactive=True)
            