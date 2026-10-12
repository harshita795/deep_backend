from enum import Enum

# A sum type represents one of several possible outcomes.
class JobOutcome:
    pass


class JobCompleted(JobOutcome):
    def __init__(self, job_id: str, records_processed: int) -> None:
        self.job_id = job_id
        self.records_processed = records_processed


class JobFailed(JobOutcome):
    def __init__(self, job_id: str, error: str) -> None:
        self.job_id = job_id
        self.error = error


def describe_job(outcome: JobOutcome) -> str:
    # Check which outcome variant was returned.
    if isinstance(outcome, JobCompleted):
        return f"Job {outcome.job_id} processed {outcome.records_processed} records"

    if isinstance(outcome, JobFailed):
        return f"Job {outcome.job_id} failed: {outcome.error}"

    raise TypeError("Unknown job outcome")


print(describe_job(JobCompleted("J101", 25)))
print(describe_job(JobFailed("J102", "Connection timeout")))


# Sum Types vs Product Types
# A sum type represents one of several alternatives.
# A product type combines multiple fields in one object.
# isinstance() helps identify which outcome we received.


#! A union type allows a function to return one of multiple types.

class ReportSuccess:
    def __init__(self, filename: str, row_count: int) -> None:
        self.filename = filename
        self.row_count = row_count


class ReportFailure:
    def __init__(self, filename: str, error: str) -> None:
        self.filename = filename
        self.error = error


# The result can be either ReportSuccess or ReportFailure.
def load_report(filename: str, content: str) -> ReportSuccess | ReportFailure:
    if content:
        return ReportSuccess(filename, len(content.splitlines()))

    return ReportFailure(filename, "File is empty")


def describe_result(result: ReportSuccess | ReportFailure) -> str:
    # Check which type of result was returned.
    if isinstance(result, ReportSuccess):
        return f"{result.filename}: {result.row_count} rows loaded"

    return f"{result.filename}: {result.error}"


print(describe_result(load_report("users.csv", "Alice\nBob")))
print(describe_result(load_report("empty.csv", "")))


# Why Union Types?
# The | operator indicates that a value can have either type.
# Union types help describe different outcomes without requiring
# the classes to share a parent class.
# Type hints help developers and type checkers; they don't enforce
# the allowed types at runtime.


#! Enum defines a fixed set of named values.
class DocType(Enum):
    PDF = 1
    TXT = 2
    DOCX = 3
    MD = 4
    HTML = 5


# Access an enum member by its name.
print(DocType.PDF)        # DocType.PDF
print(DocType.PDF.name)   # PDF
print(DocType.PDF.value)  # 1


def get_file_extension(doc_type: DocType) -> str:
    # Handle a specific enum member.
    if doc_type == DocType.PDF:
        return ".pdf"
    if doc_type == DocType.TXT:
        return ".txt"
    return "Other format"


print(get_file_extension(DocType.PDF))  # .pdf


#! Why Enums?
# Enums define a central set of valid options.
# They make code clearer than using unexplained strings or numbers.


#! Enums define the possible payment states.
class PaymentStatus(Enum):
    PENDING = 1
    PAID = 2
    FAILED = 3
    REFUNDED = 4


def get_payment_message(
    status: PaymentStatus, retry_allowed: bool
) -> str:
    # Match multiple values using a tuple.
    match (status, retry_allowed):
        case (PaymentStatus.FAILED, True):
            return "Payment failed. Retry is available."

        case (PaymentStatus.FAILED, False):
            return "Payment failed. Contact support."

        case (PaymentStatus.PAID, _):
            return "Payment successful."

        case (PaymentStatus.REFUNDED, _):
            return "Payment refunded."

        case (PaymentStatus.PENDING, _):
            return "Payment is processing."

        # Fallback for any unmatched case.
        case _:
            return "Unknown payment status."


print(get_payment_message(PaymentStatus.FAILED, True))
print(get_payment_message(PaymentStatus.PAID, False))


#! Why match?
# match/case can be clearer than long if/elif chains.
# Tuple matching checks multiple values together.
# The underscore (_) matches any value.