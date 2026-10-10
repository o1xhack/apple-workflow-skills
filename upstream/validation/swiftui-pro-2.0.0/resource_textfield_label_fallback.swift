import SwiftUI
struct Sample: View { let title: LocalizedStringResource = "Title"; @State private var text = ""; var body: some View { TextField(text: $text) { Text(title) } } }
