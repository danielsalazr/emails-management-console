
# Email management Console

This project it's been making thinking on management of several email from a company where we will can detect notifications and make automatic responses using IMAP and other technologies.

## Authors

- [@DanielSalazr](https://github.com/danielsalazr/)
- [@DanielValdes98](https://github.com/DanielValdes98)



## Tech Stack

**Client:** Angular, TailwindCSS

**Server:** Django, Celery

**Database:** Mysql


## Run Locally

Clone the project

```bash
  git clone https://github.com/danielsalazr/emails-management-console.git
```

Go to the project directory

```bash
  cd emails-management-console
```

Install virtual environment

```bash
  python3 -m venv venv
```

Start the virtual environment

```bash
  source venv/scripts/activate   (On Windows)
  source venv/bin/activate   (On Linux)
```

Install dependencies 

```bash
  pip install -r requeriments.txt
```

Run project

```bash
  Python3 manage.py runserver
```

## API Reference

#### Get latest mails

```http
  GET /emails/getMails/
```
Returns a list with latest emails in json format.

#### Get all users

```http
  GET /users/getUsers
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get an specific mail

```http
  GET /mails/getMails/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |




## Lessons Learned

We are learning new this actually and everytime.


## Roadmap

- browser support: Chrome, Firefox.

- Making new implementations anytime.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DEBUG`

`NAME_DB`

`PASSWORD_DB`

`HOST_DB`

`PORT_DB`


## Support

For support, email danielsalazr@hotmail.com or join our channels.


## Feedback

If you have any feedback, please reach out to us at danielsalazr@hotmail.com

