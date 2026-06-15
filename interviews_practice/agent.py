Create a new custom GPT.

Name it: DoD Technical Data Triage Agent

Add a short description: Reviews uploaded documents for possible DoD technical data and controlled technical information and produces evidence-based triage findings.
    
# from autogen Agent Groupchat GroupChatManager

def document_ai_reviewer(document):
    overall_prompt = '''
    You are an agent that needs to identify whether the information passed contains the following 

        1. Likely DoD Technical Data
        2. Possible DoD Technical Data
        3. Likely Controlled Technical Information
        4. Not Technical Data
        5. Insufficient Information

        DoD technical data means recorded scientific or technical information, including engineering data, drawings, specifications, technical reports, test data, maintenance instructions, repair instructions, manufacturing instructions, operational procedures, and software documentation.

        The agent must not treat the following as technical data unless the content also includes scientific or technical information:

        1. Financial information
        2. Administrative information
        3. Cost or pricing information
        4. Staffing information
        5. Management information
        6. Marketing information
        7. Contract-administration information

        Controlled technical information means technical information with military or space application that may be subject to controls on access, use, reproduction, modification, release, disclosure, or dissemination.

        The agent should pay special attention to the following indicators:
        
        1. CUI
        2. CTI
        3. CUI//SP-CTI
        4. Distribution Statement B
        5. Distribution Statement C
        6. Distribution Statement D
        7. Distribution Statement E
        8. Distribution Statement F
        9. Export-control warning
        10. Limited rights
        11. Government purpose rights
        12. Restricted rights
        13. Engineering drawings
        14. Manufacturing instructions
        15. Repair procedures
        16. Maintenance procedures
        17. Test procedures
        18. Qualification test data
        19. Military systems
        20. Space systems
        21. Weapons systems
        22. Radar systems
        23. Satellite systems
        24. Fire-control systems
        25. Tactical unmanned systems
        26. Vulnerability information involving military or space systems
        

        ## Required Agent Output
        The agent must produce the following output format:

        | Finding ID | Passage or Page | Classification | Confidence | Evidence Quote | Reason for Flag | Recommended Action |
        | ---------- | --------------- | -------------- | ---------- | -------------- | --------------- | ------------------ |


        After the table, the agent must provide:

        1. Total number of flagged passages.
        2. Highest concern level.
        3. Markings or legends detected.
        4. Whether human review is recommended.
        5. A short limitation statement.

        ## Required Limitation Statement

        The agent must include this limitation or substantially similar language:

        Included are some examples

        | Section   | Expected Result                               | Explanation                                                                                                                                            |

            |

            | Section 1 | Not Technical Data                            | Administrative, staffing, invoice, labor-hour, cost, and contract-management information                                                               |

            | Section 2 | Likely DoD Technical Data                     | Engineering drawing, dimensional tolerances, material specifications, torque values, assembly instructions, and tactical unmanned aircraft application |

            | Section 3 | Likely DoD Technical Data                     | Software documentation and test/maintenance instructions for radar equipment                                                                           |

            | Section 4 | Not Technical Data or Possible Technical Data | General commercial product information without clear military, space, CUI, CTI, export-control, or restriction indicators                              |

            | Section 5 | Likely Controlled Technical Information       | CUI//SP-CTI marking, Distribution Statement D, DoD contractor limitation, and fire-control repair procedures                                           |

            | Section 6 | Likely Controlled Technical Information       | Vulnerability details, embedded controller, satellite communications payload, reproduction steps, firmware versions, and mitigation procedures     
        
        Here is the document information to look at
        {}
        '''


    llm_config = {llm_info: [{"model_name": "gpt-4", ##}]}

    review_agent = Agent(
        name="DOD TEchnical Data Triage Agent"
        , system_prompt="Reviews uploaded documents for possible DoD technical data and controlled technical information and produces evidence-based triage findings."
        llm_config=llm_config
        )

    double_checker_agent = Agent(
        name="validator"
        , system_prompt='''This review is automated triage only. It is not a final legal, export-control, classification, CUI, contracting, or disclosure determination. Passages involving CUI, CTI, export-control indicators, military application, space application, engineering data, software documentation, vulnerability information, repair procedures, or distribution markings should be reviewed by an authorized human reviewer.
                The agent must produce the following output format:

        | Finding ID | Passage or Page | Classification | Confidence | Evidence Quote | Reason for Flag | Recommended Action |
        | ---------- | --------------- | -------------- | ---------- | -------------- | --------------- | ------------------ |
        '''
        , llm_config=llm_config
    )

    manager = GroupChatManager(name="manager", max_loops=2) # if the max_loops are then add the human in the loop


    group_chat_manager.initiate(turns="round_robin")

    chunks = # using the symantic chunker identify the different paragraphs present in the document
    for i in chunks
        group_chat_manager = GroupChatManager(
            manager=manager
            agents=[review_agent, double_checker_agent],
            prompt=overall_prompt {document}
        )
        print(review_agent.initiate(group_chat_manager)


    return review_agent.initiate(group_chat_manager)