"""Endpoint validation rejects bad submissions without hiding other errors."""

import copy
import unittest

from validate import load, reference_errors, schema_errors


class EndpointValidationTests(unittest.TestCase):
    def setUp(self):
        self.schema = load("schema.json")
        self.listing = load("data/listings/autoverzekering-nl-mcp.json")

    def references(self, listings):
        return list(reference_errors(
            listings, load("data/categories.json"), load("data/subjects.json")
        ))

    def test_malformed_endpoint_reports_schema_error_without_crashing(self):
        for value in ([], {}, 42, None):
            with self.subTest(value=value):
                listing = {**self.listing, "endpoint": value}
                listings = [(f"{listing['id']}.json", listing)]
                errors = list(schema_errors(self.schema, listings))
                self.assertTrue(any("endpoint" in error for error in errors))
                self.references(listings)

    def test_duplicate_endpoint_names_the_conflicting_listing(self):
        first = self.listing
        second = copy.deepcopy(first)
        second.update(id="another-server", source_url="https://example.com/docs")
        errors = self.references([
            (f"{first['id']}.json", first), ("another-server.json", second)
        ])
        self.assertIn(
            f"another-server.json: endpoint is a duplicate of {first['id']}.json",
            errors,
        )

    def test_source_page_cannot_also_be_the_endpoint(self):
        listing = {**self.listing, "endpoint": self.listing["source_url"]}
        errors = self.references([("autoverzekering-nl-mcp.json", listing)])
        self.assertIn(
            "autoverzekering-nl-mcp.json: endpoint is the same URL as source_url",
            errors,
        )

    def test_endpoint_requires_https_and_hosted_execution(self):
        for execution in ("local", "none", "remote", "both"):
            for endpoint in ("http://example.com/mcp", "https://example.com/mcp"):
                with self.subTest(execution=execution, endpoint=endpoint):
                    listing = {**self.listing, "execution": execution, "endpoint": endpoint}
                    errors = list(schema_errors(self.schema, [("server.json", listing)]))
                    valid = execution in ("remote", "both") and endpoint.startswith("https:")
                    self.assertEqual(not errors, valid)


if __name__ == "__main__":
    unittest.main()
