# execute this script in the blender text editor
keyconfig_version = (3, 5, 10)
keyconfig_data = \
    [("Window",
        {"space_type": 'EMPTY', "region_type": 'WINDOW'},
        {"items":
            [("wm.call_menu",
              {"type": 'N', "value": 'PRESS', "ctrl": True},
                {"properties":
                 [("name", 'TOPBAR_MT_file_new'),
                  ],
                 },
              ),
                ("wm.call_menu",
                 {"type": 'O', "value": 'PRESS', "shift": True, "ctrl": True},
                 {"properties":
                  [("name", 'TOPBAR_MT_file_open_recent'), ],
                  },
                 ),
                ("wm.open_mainfile", {"type": 'O',
                 "value": 'PRESS', "ctrl": True}, None),
                ("wm.save_mainfile", {"type": 'S',
                 "value": 'PRESS', "ctrl": True}, None),
             ("wm.save_as_mainfile", {
              "type": 'S', "value": 'PRESS', "shift": True, "ctrl": True}, None),
                ("wm.quit_blender", {"type": 'Q',
                 "value": 'PRESS', "ctrl": True}, None),
                ("wm.call_menu",
                 {"type": 'Q', "value": 'PRESS'},
                 {"properties": [("name", 'SCREEN_MT_user_menu'), ], },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F1', "value": 'PRESS', "shift": True},
                 {"properties": [("space_type", 'FILE_BROWSER'), ], },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F2', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'CLIP_EDITOR'), ],
                  },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F3', "value": 'PRESS', "shift": True},
                 {"properties": [("space_type", 'NODE_EDITOR'), ], },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F4', "value": 'PRESS', "shift": True},
                 {"properties": [("space_type", 'CONSOLE'), ], },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F5', "value": 'PRESS', "shift": True},
                 {"properties": [("space_type", 'VIEW_3D'),], },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F6', "value": 'PRESS', "shift": True},
             {"properties":
                     [("space_type", 'GRAPH_EDITOR'),
                      ],
              },
            ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F7', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'PROPERTIES'),
                   ],
                  },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F8', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'SEQUENCE_EDITOR'),
                   ],
                  },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F9', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'OUTLINER'),
                   ],
                  },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F10', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'IMAGE_EDITOR'),
                   ],
                  },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F11', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'TEXT_EDITOR'),
                   ],
                  },
                 ),
                ("screen.space_type_set_or_cycle",
                 {"type": 'F12', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("space_type", 'DOPESHEET_EDITOR'),
                   ],
                  },
                 ),
                ("wm.call_panel",
                 {"type": 'NDOF_BUTTON_MENU', "value": 'PRESS'},
                 {"properties":
                  [("name", 'USERPREF_PT_ndof_settings'),
                   ],
                  },
                 ),
                ("wm.context_scale_float",
                 {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS'},
                 {"properties":
                  [("data_path", 'preferences.inputs.ndof_sensitivity'),
                   ("value", 1.1),
                   ],
                  },
                 ),
                ("wm.context_scale_float",
                 {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS'},
                 {"properties":
                  [("data_path", 'preferences.inputs.ndof_sensitivity'),
                   ("value", 0.90909094),
                   ],
                  },
                 ),
                ("wm.context_scale_float",
                 {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("data_path", 'preferences.inputs.ndof_sensitivity'),
                   ("value", 1.5),
                   ],
                  },
                 ),
                ("wm.context_scale_float",
                 {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS', "shift": True},
                 {"properties":
                  [("data_path", 'preferences.inputs.ndof_sensitivity'),
                   ("value", 0.6666667),
                   ],
                  },
                 ),
                ("info.reports_display_update", {
                 "type": 'TIMER_REPORT', "value": 'ANY', "any": True}, None),
                ("wm.doc_view_manual_ui_context", {
                    "type": 'F1', "value": 'PRESS'}, None),
                ("wm.call_panel",
                 {"type": 'F2', "value": 'PRESS'},
                 {"properties":
                  [("name", 'TOPBAR_PT_name'),
                   ("keep_open", False),
                   ],
                  },
                 ),
                ("wm.batch_rename", {"type": 'F2',
                                     "value": 'PRESS', "ctrl": True}, None),
                ("wm.search_menu", {"type": 'SEMI_COLON',
                                    "value": 'PRESS', "shift": True}, None),
                ("wm.call_menu",
                 {"type": 'F4', "value": 'PRESS'},
                 {"properties":
                     [("name", 'TOPBAR_MT_file_context_menu'),
                      ],
                  },
                 ),
                ("wm.toolbar_fallback_pie", {"type": 'W',
                                             "value": 'PRESS', "alt": True}, None),
                ("wm.toolbar", {"type": 'SPACE',
                                "value": 'PRESS', "shift": True}, None),
            ],
         },
      ),
     ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
