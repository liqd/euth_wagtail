import rules
from rules.predicates import is_superuser

from euth.modules.predicates import (is_context_member, is_context_moderator,
                                     is_public_context)
from euth.phases.predicates import phase_allows_comment

rules.add_perm('euth_documents.comment_paragraph',
               is_superuser | is_context_moderator |
               (is_context_member & phase_allows_comment))

rules.add_perm('euth_documents.comment_document',
               is_superuser | is_context_moderator |
               (is_context_member & phase_allows_comment))

rules.add_perm('euth_documents.view_paragraph',
               is_superuser | is_context_moderator |
               is_context_member | is_public_context)