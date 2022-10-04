import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ADDRESS, CONF_ID


boilerplate_ns = cg.esphome_ns.namespace("boilerplate")
boilerplateComponent = boilerplate_ns.class_("Boilerplate", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(boilerplateComponent),
    }
).extend(cv.COMPONENT_SCHEMA)

MULTI_CONF = True
CODEOWNERS = ["@jpeletier"]


async def to_code(config):

    id = config[CONF_ID]
    server = cg.new_Pvariable(id)

    await cg.register_component(server, config)

    return
