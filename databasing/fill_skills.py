from DatabaseConnect import DatabaseConnect

"""Attributes
stamina, focus, confidence, head, body, legs, arms
"""
fitness_list = {
        "level" : "level1",
        "standard" : "fitness",
        "strokes" : {
            "flutter_kick_5m_assisted" : [
                {
                    "skill" : "horizontal_body_position",
                    "attribute" : [0,0,0,0,1,0,0]
                },
                {
                    "skill" : "front_or_back_kick",
                    "attribute" : [0,0,0,0,0,1,0]
                },
                {
                    "skill" : "kick_from_hip",
                    "attribute" : [0,0,0,0,0,1,0]
                },
                {
                    "skill" : "vertical_leg_motion",
                    "attribute" : [0,0,0,0,0,1,0]
                },
                {
                    "skill" : "completed_distance",
                    "attribute" : [1,0,0,0,0,0,0]
                },
            ],
            "distance_swim_5m" : [
                {
                    "skill" : "front_or_back_swim",
                    "attribute" : [0,0,0,0,1,0,0]
                },
                {
                    "skill" : "arm_leg_movement",
                    "attribute" : [0,0,0,0,0,1,1]
                },
                {
                    "skill" : "body_position_w_flutter_kick",
                    "attribute" : [0,0,0,0,1,1,1]
                },
                {
                    "skill" : "horizontal_body_position",
                    "attribute" : [0,0,0,0,1,0,0]
                },
                {
                    "skill" : "exhale_underwater",
                    "attribute" : [0,0,1,1,0,0,0]
                },
                {
                    "skill" : "completed_distance",
                    "attribute" : [1,0,0,0,0,0,0]
                },
            ],
        }
    }

safety_list = {
        "level" : "level1",
        "standard" : "safety",
        "strokes" : {
            "facility_site_orientation" : [
                {
                    "skill" : "identifies_safety_and_hazards",
                    "attribute" : [0,1,0,0,0,0,0]
                },
                {
                    "skill" : "waits_for_instructor",
                    "attribute" : [0,1,0,0,0,0,0]
                }
            ],
            "supervision" : [
                {
                    "skill" : "explains_supervision",
                    "attribute" : [0,1,0,0,0,0,0]
                }
            ],
            "shallow_entries_exits" : [
                {
                    "skill" : "waits_for_instructor",
                    "attribute" : [0,1,0,0,0,0,0]
                },
                {
                    "skill" : "performs_safe_entries_exits",
                    "attribute" : [0,1,0,0,0,0,0]
                },
                {
                    "skill" : "performs_safe_exits",
                    "attribute" : [0,1,0,0,0,0,0]
                }
            ],
            "submerge_head" : [
                {
                    "skill" : "head_underwater_3sec",
                    "attribute" : [0,0,1,1,0,0,0]
                },
                {
                    "skill" : "eyes_open_underwater",
                    "attribute" : [0,0,1,1,0,0,0]
                },
            ],
            "exhale_through_mouth_nose" : [
                {
                    "skill" : "exhale_below_surface",
                    "attribute" : [0,0,1,1,0,0,0]
                },
                {
                    "skill" : "exhale_w_head_underwater",
                    "attribute" : [0,0,1,1,0,0,0]
                },
            ]
        }
    }

swimming_list = {
        "level" : "level1",
        "standard" : "swimming",
        "strokes" : {
            "rhythmic_breathing_5_times" : [
                {
                    "skill" : "exhale_underwater_inhale_air",
                    "attribute" : [0,0,0,1,0,0,0]
                },
                {
                    "skill" : "rhythmic_relaxed",
                    "attribute" : [0,0,1,1,0,0,0]
                },
                {
                    "skill" : "5_repetitions",
                    "attribute" : [1,0,0,0,0,0,0]
                }
            ],
            "front_float_recovery_3sec" : [
                {
                    "skill" : "stable_face_in_water",
                    "attribute" : [0,0,1,1,1,0,0]
                },
                {
                    "skill" : "float_3sec_relaxed",
                    "attribute" : [1,0,1,1,1,0,0]
                },
                {
                    "skill" : "vertical_recovery",
                    "attribute" : [0,0,1,0,1,1,0]
                }
            ],
            "front_glide_5sec" : [
                {
                    "skill" : "glide_5sec_relaxed",
                    "attribute" : [1,0,1,1,0,0,0]
                },
                {
                    "skill" : "streamlined_body_position",
                    "attribute" : [0,0,0,1,1,1,1]
                },
                {
                    "skill" : "vertical_recovery",
                    "attribute" : [0,0,1,0,1,1,0]
                }
            ],
            "front_glide_kick_5m" : [
                {
                    "skill" : "vertical_leg_motion",
                    "attribute" : [0,0,0,0,0,1,0]
                },
                {
                    "skill" : "kicks_5m_horizontal_body",
                    "attribute" : [1,0,0,0,1,1,0]
                },
                {
                    "skill" : "streamlined_body_position",
                    "attribute" : [0,0,0,1,1,1,1]
                },
                {
                    "skill" : "exhale_underwater",
                    "attribute" : [0,0,0,1,0,0,0]
                }
            ],
            "back_float_recovery_3sec" : [
                {
                    "skill" : "stable_back_float",
                    "attribute" : [0,0,1,1,1,0,0]
                },
                {
                    "skill" : "float_3sec_relaxed",
                    "attribute" : [1,0,1,1,1,0,0]
                },
                {
                    "skill" : "vertical_recovery",
                    "attribute" : [0,0,1,0,1,1,0]
                }     
            ],
            "back_glide_5sec" : [
                {
                    "skill" : "glide_5sec_relaxed",
                    "attribute" : [1,0,1,1,1,0,0]
                },
                {
                    "skill" : "streamlined_body_position",
                    "attribute" : [0,0,0,1,1,1,1]
                },
                {
                    "skill" : "vertical_recovery",
                    "attribute" : [0,0,1,0,1,1,0]
                }
            ],
            "rollover_glide_5sec_assisted" : [
                {
                    "skill" : "rolls_front_to_back",
                    "attribute" : [0,0,1,1,1,0,0]
                },
                {
                    "skill" : "exhale_underwater_inhale_air",
                    "attribute" : [0,0,1,1,0,0,0]
                },
                {
                    "skill" : "rolls_back_to_front",
                    "attribute" : [0,0,1,1,1,0,0]
                },
                {
                    "skill" : "streamlined_body_position",
                    "attribute" : [0,0,0,1,1,1,1]
                },
                {
                    "skill" : "starts_roll_head_shoulders",
                    "attribute" : [0,0,0,1,0,0,1]
                },
                {
                    "skill" : "vertical_recovery",
                    "attribute" : [0,0,1,0,1,1,0]
                }
            ],
            "front_swim_5m" : [
                {
                    "skill" : "arm_leg_movement",
                    "attribute" : [0,0,0,0,0,1,1]
                },
                {
                    "skill" : "completed_distance",
                    "attribute" : [1,0,0,0,0,0,0]
                },
            ]
        }
    }

db = DatabaseConnect("level_one.db")
db.multifill_skills(fitness_list)
db.multifill_skills(safety_list)
db.multifill_skills(swimming_list)