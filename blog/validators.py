def validate_contact_form(data):
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    message = data.get("message")
    d = {
    'Ok':False
    }
    if len(name) < 2:
        d["Error"] = "Name should be at least 2 characters"
        return d
    if (email.count('@') != 1 or is_valid_email(email[:email.find('@')]) or
            email[email.find('@') + 1:].count('.') != 1):
        d["Error"] = "Email is not valid"
        return d
    if len(message) < 5:
        d["Error"] = "Message should be at least 5 characters"
        return d
    if phone[:4] !='+998' or len(phone) !=13:
        d["Error"] = "Entered number is not valid"
        return d
    d['Ok']=True
    return d
def is_valid_email(text):
    if not text[0].isalpha():
        return True
    for i in text:
        if i in ['&', '+', '=', '_', '<', '>', '`', '¬', '*']:
            return True
        return False
