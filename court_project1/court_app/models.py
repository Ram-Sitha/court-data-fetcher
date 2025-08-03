from django.db import models

class CaseQuery(models.Model):
    case_type=models.CharField(max_length=50)
    case_number=models.CharField(max_length=50)
    filing_year=models.CharField(max_length=4)
    raw_response=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.case_type}-{self.case_number} ({self.filing_year})"
