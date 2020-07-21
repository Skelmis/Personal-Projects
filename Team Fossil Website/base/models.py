from djongo import models

class Partner(models.Model):
    """
    Handles each of our partners

    Each partner should have:
     - name (There name / company name)
     - image (Something that represents them, a default is provided)
     - description (Who they are or whatever)
     - link (A link to there site, youtube, whatever)
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    link = models.CharField(max_length=100)
    image = models.ImageField(default='b_map3.png', upload_to='partnerPictures')

    def __str__(self):
        return f"Partner: {self.name}"


class TeamMember(models.Model):
    """
    Handles a member of our team

    Each team member should have:
     - displayName (Generally ign)
     - quote (quote, favorite saying)
     - character (Who they main)
     - content (A bit about them)
    """
    BANGALORE = 'Bangalore'
    BLOODHOUND = 'Bloodhound'
    CAUSTIC = "Caustic"
    CRYPTO = 'Crypto'
    GIBRALTER = 'Gibralter'
    LIFELINE = 'Lifeline'
    LOBA = 'Loba'
    MIRAGE = 'Mirage'
    OCTANE = 'Octance'
    PATHFINDER = 'Pathfinder'
    REVENANT = 'Revenant'
    WATTSON = 'Wattson'
    WRAITH = 'Wraith'

    LEGENDS = (
        (BANGALORE, BANGALORE),
        (BLOODHOUND, BLOODHOUND),
        (CAUSTIC, CAUSTIC),
        (CRYPTO, CRYPTO),
        (GIBRALTER, GIBRALTER),
        (LIFELINE, LIFELINE),
        (LOBA, LOBA),
        (MIRAGE, MIRAGE),
        (OCTANE, OCTANE),
        (PATHFINDER, PATHFINDER),
        (REVENANT, REVENANT),
        (WATTSON, WATTSON),
        (WRAITH, WRAITH)
    )

    ign = models.CharField(max_length=50)
    quote = models.CharField(max_length=100)
    character = models.CharField(max_length=15, choices=LEGENDS, default=MIRAGE)
    content = models.TextField(max_length=500)
    profilePicture = models.ImageField(default='default.jpg', upload_to='teamPictures')

    def __str__(self):
        return f"TeamMember: {self.ign}"
