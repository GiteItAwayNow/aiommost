from aiommost import schemas
from aiommost.client import MattermostClient


async def test_user_created(client: MattermostClient, fake):
    username, email, password = fake.pystr().lower(), fake.email(), fake.password()

    user = await client.users.create(username, email, password)
    assert user.username == username


async def test_user_deleted(client: MattermostClient, fake):
    username, email, password = fake.pystr(), fake.email(), fake.password()

    user = await client.users.create(username, email, password)

    await client.users.delete(user.uid)


async def test_get_by_username(client: MattermostClient, create_user):
    existing_user: schemas.User = await create_user()

    user = await client.users.get_by_username(existing_user.username)
    assert user.username == existing_user.username


async def test_get_by_usernames(client: MattermostClient, create_user):
    first_user: schemas.User = await create_user()
    second_user: schemas.User = await create_user()

    users = await client.users.get_by_usernames([first_user.username, second_user.username])
    assert len(users) == 2
