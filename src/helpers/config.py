import os
from dotenv import dotenv_values

config: dict[str, str] = {
    # load shared development variables
    **{k: v if v is not None else '' for k, v in dotenv_values(".env.shared").items()},

    # load sensitive variables
    **{k: v if v is not None else '' for k, v in dotenv_values(".env.secret").items()},

    # override loaded values with environment variables
    **{k: v if v is not None else '' for k, v in os.environ.items()},
}
